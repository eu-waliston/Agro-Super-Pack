import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function ScoreScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Score Detalhado</Text>
      <Text style={styles.text}>
        Aqui você pode colocar gráfico e métricas completas.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#0B0F14",
    padding: 24,
  },
  title: {
    fontSize: 22,
    color: "#00FF88",
    marginBottom: 16,
  },
  text: {
    color: "#ccc",
  },
});
