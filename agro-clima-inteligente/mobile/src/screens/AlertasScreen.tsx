import React, { useState } from "react";
import { View, Text, StyleSheet, TouchableOpacity, ScrollView } from "react-native";
import { Ionicons } from "@expo/vector-icons";

export function AlertasScreen() {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.titulo}>Alertas</Text>

      <View style={[styles.card, styles.alertaVermelho]}>
        <View style={styles.alertaHeader}>
          <Ionicons name="alert-circle" size={22} color="#fff" />
          <Text style={styles.cardTitulo}>Baixa Umidade</Text>
        </View>
        <Text style={styles.cardItem}>
          A umidade caiu abaixo de 40%. Recomenda-se irrigação imediata.
        </Text>
      </View>

      <View style={[styles.card, styles.alertaAmarelo]}>
        <View style={styles.alertaHeader}>
          <Ionicons name="warning" size={22} color="#fff" />
          <Text style={styles.cardTitulo}>Temperatura Elevada</Text>
        </View>
        <Text style={styles.cardItem}>
          Temperatura acima do ideal para o cultivo atual.
        </Text>
      </View>

      <View style={[styles.card, styles.alertaVerde]}>
        <View style={styles.alertaHeader}>
          <Ionicons name="checkmark-circle" size={22} color="#fff" />
          <Text style={styles.cardTitulo}>Sistema Operacional</Text>
        </View>
        <Text style={styles.cardItem}>
          Todos os sensores estão funcionando corretamente.
        </Text>
      </View>
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