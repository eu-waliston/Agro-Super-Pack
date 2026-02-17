import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import DetalhesScreen from '../src/screens/DetalhesScreen';
import {AlertasScreen} from '../src/screens/AlertasScreen';

import HomeScreen from '../src/screens/HomeScreen';
import HistoricoScreen from '../src/screens/HistoricoScreen';

const Drawer = createDrawerNavigator();
const Stack = createNativeStackNavigator();

function DrawerRoutes() {
  return (
    <Drawer.Navigator
      screenOptions={{
        headerShown: true,
      }}
      id="DrawerNavigator"
    >
      <Drawer.Screen name="Home" component={HomeScreen} />
      <Drawer.Screen name="Histórico" component={HistoricoScreen} />
      <Drawer.Screen name="Detalhes" component={DetalhesScreen} />
      <Drawer.Screen name="Alertas" component={AlertasScreen} />
    </Drawer.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <DrawerRoutes />
    </NavigationContainer>
  );
}