import {useEffect, useState, useCallback} from "react";
import {
    View,
    Text,
    ActivityIndicator,
    ScrollView,
    StyleSheet,
    RefreshControl,
    Dimensions,
} from "react-native";

import {Picker} from "@react-native-picker/picker";
import {LineChart} from "react-native-chart-kit";
import {LinearGradient} from "expo-linear-gradient";
import * as Location from "expo-location";

import {getWeather, getWeatherByCoords} from "../services/api";
import {WeatherResponse} from "../types/weather";
import ScoreCard from "../components/ScoreCard";

export default function HomeScreen() {
    const [data, setData] = useState<WeatherResponse | null>(null);
    const [loading, setLoading] = useState(true);
    const [refreshing, setRefreshing] = useState(false);

    const [selectedCity, setSelectedCity] = useState("Sorriso");
    const [selectedCulture, setSelectedCulture] = useState("milho");

    const screenWidth = Dimensions.get("window").width;

    // 🔥 Busca por cidade
    const loadWeather = useCallback(async () => {
        try {
            const response = await getWeather(selectedCity, selectedCulture);
            setData(response);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
            setRefreshing(false);
        }
    }, [selectedCity, selectedCulture]);

    // 🔥 Busca por localização automática
    const getUserLocation = useCallback(async () => {
        try {
            let {status} = await Location.requestForegroundPermissionsAsync();

            if (status !== "granted") {
                loadWeather(); // fallback
                return;
            }

            const location = await Location.getCurrentPositionAsync({});
            const {latitude, longitude} = location.coords;

            const response = await getWeatherByCoords(
                latitude,
                longitude,
                selectedCulture
            );

            setData(response);
        } catch (error) {
            console.error(error);
            loadWeather(); // fallback
        } finally {
            setLoading(false);
        }
    }, [loadWeather, selectedCulture]);

    useEffect(() => {
        setLoading(true);
        getUserLocation();
    }, [getUserLocation]);

    async function onRefresh() {
        setRefreshing(true);
        loadWeather();
    }

    if (loading) {
        return (
            <View style={styles.center}>
                <ActivityIndicator size="large" color="#2E7D32"/>
            </View>
        );
    }

    if (!data) {
        return (
            <View style={styles.center}>
                <Text>Erro ao carregar dados</Text>
            </View>
        );
    }

    const chartData = {
        labels: data.previsao_proximas_horas.map((item) => item.hora),
        datasets: [
            {
                data: data.previsao_proximas_horas.map(
                    (item) => item.temperatura
                ),
            },
        ],
    };

    return (
        <LinearGradient
            colors={["#E8F5E9", "#FFFFFF"]}
            style={{flex: 1}}
        >
            <ScrollView
                contentContainerStyle={styles.container}
                showsVerticalScrollIndicator={false}
                refreshControl={
                    <RefreshControl refreshing={refreshing} onRefresh={onRefresh}/>
                }
            >
                {/* 📍 Cidade */}
                <Text style={{fontSize: 14, marginBottom: 5, opacity: 0.6}}>
                    📍 Selecionar Cidade
                </Text>
                <View style={styles.cardBase}>
                    <Picker
                        selectedValue={selectedCity}
                        onValueChange={(itemValue) => setSelectedCity(itemValue)}
                    >
                        <Picker.Item label="Sorriso" value="Sorriso"/>
                        <Picker.Item label="Lucas do Rio Verde" value="Lucas do Rio Verde"/>
                        <Picker.Item label="Cuiabá" value="Cuiabá"/>
                    </Picker>
                </View>

                {/* 🌱 Cultura */}
                <Text style={styles.label}>🌱 Selecionar Cultura</Text>
                <View style={styles.cardBase}>
                    <Picker
                        selectedValue={selectedCulture}
                        onValueChange={(itemValue) => setSelectedCulture(itemValue)}
                    >
                        <Picker.Item label="Milho" value="milho"/>
                        <Picker.Item label="Soja" value="soja"/>
                        <Picker.Item label="Trigo" value="trigo"/>
                    </Picker>
                </View>

                {/* 🌡️ Hero */}
                <Text style={styles.culture}>
                    {data.cultura.toUpperCase()}
                </Text>

                <Text style={styles.temperature}>
                    {data.temperatura_atual}°C
                </Text>

                <Text style={styles.wind}>
                    💨 {data.vento_kmh} km/h
                </Text>

                {/* 📊 Score */}
                <View style={styles.cardBase}>
                    <ScoreCard score={data.score_climatico}/>
                </View>

                {/* 🔔 Alertas */}
                <Text style={styles.sectionTitle}>🔔 Alertas</Text>

                {data.alertas.length === 0 ? (
                    <View style={styles.cardBase}>
                        <Text style={{textAlign: "center"}}>
                            Nenhum alerta ativo 🙌
                        </Text>
                    </View>
                ) : (
                    data.alertas.map((alerta, index) => (
                        <View key={index} style={styles.alertCard}>
                            <Text style={styles.alertText}>⚠ {alerta}</Text>
                        </View>
                    ))
                )}

                {/* 📊 Gráfico */}
                <Text style={styles.sectionTitle}>
                    📊 Temperatura nas Próximas Horas
                </Text>

                <View style={styles.cardBase}>
                    <LineChart
                        data={chartData}
                        width={screenWidth - 80}
                        height={220}
                        chartConfig={{
                            backgroundGradientFrom: "#FFFFFF",
                            backgroundGradientTo: "#FFFFFF",
                            decimalPlaces: 1,
                            color: (opacity = 1) =>
                                `rgba(46, 125, 50, ${opacity})`,
                            labelColor: (opacity = 1) =>
                                `rgba(0, 0, 0, ${opacity})`,
                        }}
                        bezier
                        style={{borderRadius: 16}}
                    />
                </View>
            </ScrollView>
        </LinearGradient>
    );
}

const styles = StyleSheet.create({
    container: {
        padding: 20,
        paddingBottom: 40,
    },

    center: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
    },

    label: {
        fontSize: 14,
        marginBottom: 6,
        marginTop: 10,
        opacity: 0.6,
    },

    culture: {
        fontSize: 18,
        textAlign: "center",
        marginTop: 20,
        opacity: 0.7,
        letterSpacing: 1,
    },

    temperature: {
        fontSize: 82,
        fontWeight: "800",
        textAlign: "center",
        color: "#111827",
    },

    wind: {
        textAlign: "center",
        marginBottom: 20,
        opacity: 0.7,
    },

    sectionTitle: {
        fontSize: 20,
        fontWeight: "700",
        marginTop: 25,
        marginBottom: 10,
    },

    cardBase: {
        backgroundColor: "#FFFFFF",
        padding: 18,
        borderRadius: 20,
        marginBottom: 15,
        shadowColor: "#000",
        shadowOffset: {width: 0, height: 6},
        shadowOpacity: 0.1,
        shadowRadius: 10,
        elevation: 5,
    },

    alertCard: {
        backgroundColor: "#FFEAEA",
        padding: 15,
        borderRadius: 16,
        marginBottom: 10,
    },

    alertText: {
        color: "#D32F2F",
        fontWeight: "600",
    },
});
