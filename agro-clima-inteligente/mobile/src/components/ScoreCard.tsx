import { useEffect, useRef } from "react";
import { View, Text, Animated, StyleSheet } from "react-native";

interface Props {
  score: number;
}

export default function ScoreCard({ score }: Props) {
  const animatedValue = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(animatedValue, {
      toValue: score,
      duration: 1000,
      useNativeDriver: false,
    }).start();
  }, [score]);

  return (
    <View style={styles.container}>
      <Animated.Text style={styles.score}>
        {animatedValue.interpolate({
          inputRange: [0, 100],
          outputRange: ["0", score.toString()],
        })}
      </Animated.Text>
      <Text style={styles.label}>Score Climático</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#fff",
    padding: 20,
    borderRadius: 16,
    alignItems: "center",
    elevation: 3,
  },
  score: {
    fontSize: 40,
    fontWeight: "bold",
  },
  label: {
    marginTop: 5,
    fontSize: 14,
    opacity: 0.6,
  },
});
