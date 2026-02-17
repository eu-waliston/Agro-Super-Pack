export interface ForecastHour {
  hora: string;
  temperatura: number;
  vento: number;
  chuva_mm: number;
}

export interface WeatherResponse {
  latitude: number;
  longitude: number;
  cultura: string;
  temperatura_atual: number;
  vento_kmh: number;
  alertas: string[];
  score_climatico: number;
  previsao_proximas_horas: ForecastHour[];
}
