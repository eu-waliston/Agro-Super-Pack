import React, { useEffect, useRef } from "react";
import { Animated, Text, StyleSheet } from "react-native";

type Props = {
  visible: boolean;
  message: string;
  color: string;
};

export default function BannerAlert({
  visible,
  message,
  color,
}: Props) {
  const slideAnim = useRef(new Animated.Value(-120)).current;

  useEffect(() => {
    if (visible) {
      Animated.timing(slideAnim, {
        toValue: 0,
        duration: 400,
        useNativeDriver: true,
      }).start();

      const timeout = setTimeout(() => {
        Animated.timing(slideAnim, {
          toValue: -120,
          duration: 400,
          useNativeDriver: true,
        }).start();
      }, 4000);

      return () => clearTimeout(timeout);
    }
  }, [visible]);

  return (
    <Animated.View
      style={[
        styles.banner,
        { backgroundColor: color, transform: [{ translateY: slideAnim }] },
      ]}
    >
      <Text style={styles.text}>{message}</Text>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  banner: {
    position: "absolute",
    top: 0,
    width: "100%",
    padding: 18,
    zIndex: 999,
  },
  text: {
    color: "#fff",
    fontWeight: "bold",
    textAlign: "center",
  },
});
