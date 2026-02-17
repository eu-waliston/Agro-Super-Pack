import { createDrawerNavigator } from "@react-navigation/drawer";
import HomeScreen from "../screens/HomeScreen";
import ScoreScreen from "../screens/ScoreScreen";
import HistoricoScreen from "../screens/HistoricoScreen";
import ConfigScreen from "../screens/ConfigScreen";

const Drawer = createDrawerNavigator();

export default function DrawerNavigator() {
  return (
    <Drawer.Navigator
      id="MainDrawer"
      screenOptions={{
        headerShown: false,
        drawerStyle: {
          backgroundColor: "#0B0F14",
        },
        drawerActiveTintColor: "#00FF88",
        drawerInactiveTintColor: "#aaa",
      }}
    >
      <Drawer.Screen name="Home" component={HomeScreen} />
      <Drawer.Screen name="Score" component={ScoreScreen} />
      <Drawer.Screen name="Histórico" component={HistoricoScreen} />
      <Drawer.Screen name="Configurações" component={ConfigScreen} />
    </Drawer.Navigator>
  );
}
