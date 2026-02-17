import React from "react";
import { View, Text, StyleSheet, TouchableOpacity } from "react-native";
import { LinearGradient } from "expo-linear-gradient";
import { useNavigation } from "@react-navigation/native";

export default function HomeScreen() {
  const userName = "Waliston"; // depois podemos pegar dinâmico
  const score = 82;
  const clima = "Parcialmente nublado";
  const temperatura = 27;
  const navigation = useNavigation<any>();

  return (
    <LinearGradient
      colors={["#0B0F14", "#101820"]}
      style={styles.container}
    >
      {/* 👋 Saudação */}
      <Text style={styles.greeting}>
        Olá, {userName} 👋
      </Text>

      {/* 🌤 Status principal */}
      <Text style={styles.status}>
        {clima} • {temperatura}°
      </Text>

      {/* 🎯 Score */}
      <View style={styles.scoreContainer}>
        <Text style={styles.score}>{score}</Text>
        <Text style={styles.scoreLabel}>Agro Score</Text>
      </View>

      {/* ⚡ Ações rápidas */}
      <View style={styles.actions}>
        <TouchableOpacity
          style={styles.actionButton}
          onPress={() => navigation.navigate('Detalhes')}
        >
          <Text style={styles.actionText}>Ver Detalhes</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.actionButton}
          onPress={() => navigation.navigate('Histórico')}
        >
          <Text style={styles.actionText}>Histórico</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.actionButton}
          onPress={() => navigation.navigate('Alertas')}
        >
          <Text style={styles.actionText}>Alertas</Text>
        </TouchableOpacity>
      </View>

    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 24,
    justifyContent: "center",
  },
  greeting: {
    color: "#aaa",
    fontSize: 18,
    marginBottom: 8,
  },
  status: {
    color: "#00FF88",
    fontSize: 16,
    marginBottom: 40,
  },
  scoreContainer: {
    alignItems: "center",
    marginBottom: 40,
  },
  score: {
    fontSize: 72,
    color: "#00FF88",
    fontWeight: "bold",
  },
  scoreLabel: {
    color: "#888",
    fontSize: 16,
  },
  actions: {
    gap: 16,
  },
  actionButton: {
    borderWidth: 1,
    borderColor: "#00FF88",
    padding: 14,
    borderRadius: 12,
  },
  actionText: {
    color: "#00FF88",
    textAlign: "center",
  },
});
