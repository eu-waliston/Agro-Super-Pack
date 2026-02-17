import React, { useState } from "react";
import { View, Text, StyleSheet, TouchableOpacity, ScrollView } from "react-native";
import { Ionicons } from "@expo/vector-icons";

export default function DetalhesScreen() {
  const [abaAtiva, setAbaAtiva] = useState<"cultivo" | "irrigacao">("cultivo");

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.titulo}>Detalhes</Text>

      <View style={styles.tabsContainer}>
        <TouchableOpacity
          style={[styles.tabButton, abaAtiva === "cultivo" && styles.tabAtiva]}
          onPress={() => setAbaAtiva("cultivo")}
        >
          <Ionicons name="leaf" size={18} color="#fff" />
          <Text style={styles.tabText}>Cultivo</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.tabButton, abaAtiva === "irrigacao" && styles.tabAtiva]}
          onPress={() => setAbaAtiva("irrigacao")}
        >
          <Ionicons name="water" size={18} color="#fff" />
          <Text style={styles.tabText}>Irrigação</Text>
        </TouchableOpacity>
      </View>

      {abaAtiva === "cultivo" && (
        <View style={styles.card}>
          <Text style={styles.cardTitulo}>Status do Cultivo</Text>
          <Text style={styles.cardItem}>🌾 Crescimento: 78%</Text>
          <Text style={styles.cardItem}>🌡️ Temperatura do Solo: 24°C</Text>
          <Text style={styles.cardItem}>🧪 Nutrientes: Nível ideal</Text>
        </View>
      )}

      {abaAtiva === "irrigacao" && (
        <View style={styles.card}>
          <Text style={styles.cardTitulo}>Sistema de Irrigação</Text>
          <Text style={styles.cardItem}>💧 Umidade do Solo: 65%</Text>
          <Text style={styles.cardItem}>🚿 Última Irrigação: 2h atrás</Text>
          <Text style={styles.cardItem}>⚙️ Status: Operando normalmente</Text>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: "#0f172a",
    flexGrow: 1,
  },
  titulo: {
    fontSize: 26,
    fontWeight: "bold",
    color: "#fff",
    marginBottom: 20,
  },
  tabsContainer: {
    flexDirection: "row",
    gap: 10,
    marginBottom: 20,
  },
  tabButton: {
    flexDirection: "row",
    alignItems: "center",
    gap: 6,
    paddingVertical: 10,
    paddingHorizontal: 14,
    backgroundColor: "#334155",
    borderRadius: 12,
  },
  tabAtiva: {
    backgroundColor: "#16a34a",
  },
  tabText: {
    color: "#fff",
    fontWeight: "600",
  },
  card: {
    backgroundColor: "#1e293b",
    padding: 16,
    borderRadius: 16,
    marginBottom: 16,
  },
  cardTitulo: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#fff",
    marginBottom: 8,
  },
  cardItem: {
    color: "#cbd5e1",
    marginBottom: 4,
  },
  alertaHeader: {
    flexDirection: "row",
    alignItems: "center",
    gap: 8,
    marginBottom: 6,
  },
  alertaVermelho: {
    borderLeftWidth: 5,
    borderLeftColor: "#ef4444",
  },
  alertaAmarelo: {
    borderLeftWidth: 5,
    borderLeftColor: "#facc15",
  },
  alertaVerde: {
    borderLeftWidth: 5,
    borderLeftColor: "#22c55e",
  },
});
