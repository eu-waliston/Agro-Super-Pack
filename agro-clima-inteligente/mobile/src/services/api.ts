let BASE_URL = "http://192.168.11.101:8000";

const cityCoordinates: Record<string, { lat: number; lon: number }> = {
    Sorriso: {lat: -12.54, lon: -55.72},
    "Lucas do Rio Verde": {lat: -13.05, lon: -55.90},
    Cuiabá: {lat: -15.60, lon: -56.10},
};

export async function getWeatherByCoords(
  lat: number,
  lon: number,
  cultura: string = "milho"
) {
  const response = await fetch(
    `${BASE_URL}/clima?lat=${lat}&lon=${lon}&cultura=${cultura}`
  );

  if (!response.ok) {
    throw new Error("Erro ao buscar clima");
  }

  return response.json();
}


export async function getWeather(
    city: string,
    cultura: string = "milho"
) {
    const coords = cityCoordinates[city];

    if (!coords) {
        throw new Error("Cidade não encontrada");
    }


    const response = await fetch(
        `${BASE_URL}/clima?lat=${coords.lat}&lon=${coords.lon}&cultura=${cultura}`
    );

    if (!response.ok) {
        throw new Error("Erro ao buscar clima");
    }

    return response.json();
}


