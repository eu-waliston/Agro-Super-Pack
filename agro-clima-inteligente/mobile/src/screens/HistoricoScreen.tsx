import React from "react";
import { View, Text, StyleSheet, ScrollView } from "react-native";
import { LineChart } from "react-native-chart-kit";
import { Dimensions } from "react-native";

const screenWidth = Dimensions.get("window").width;

export default function HistoricoScreen() {
  const dadosScore = [65, 70, 75, 72, 80, 85, 82];

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Histórico Agro Score</Text>

      {/* 📈 Gráfico */}
      <LineChart
        data={{
          labels: ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"],
          datasets: [
            {
              data: dadosScore,
            },
          ],
        }}
        width={screenWidth - 32}
        height={220}
        yAxisSuffix=""
        chartConfig={{
          backgroundColor: "#0B0F14",
          backgroundGradientFrom: "#0B0F14",
          backgroundGradientTo: "#0B0F14",
          decimalPlaces: 0,
          color: (opacity = 1) => `rgba(0, 255, 136, ${opacity})`,
          labelColor: () => "#aaa",
          propsForDots: {
            r: "4",
            strokeWidth: "2",
            stroke: "#00FF88",
          },
        }}
        bezier
        style={styles.chart}
      />

      {/* 📋 Lista de registros */}
      <View style={styles.recordsContainer}>
        {dadosScore.map((valor, index) => (
          <View key={index} style={styles.recordItem}>
            <Text style={styles.recordDate}>
              Dia {index + 1}
            </Text>
            <Text style={styles.recordValue}>
              {valor}
            </Text>
          </View>
        ))}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#0B0F14",
    padding: 16,
  },
  title: {
    fontSize: 22,
    color: "#00FF88",
    marginBottom: 24,
  },
  chart: {
    borderRadius: 16,
  },
  recordsContainer: {
    marginTop: 32,
  },
  recordItem: {
    flexDirection: "row",
    justifyContent: "space-between",
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: "#1a1f24",
  },
  recordDate: {
    color: "#aaa",
  },
  recordValue: {
    color: "#00FF88",
    fontWeight: "bold",
  },
});
