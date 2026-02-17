export type DadosIrrigacao = {
  temperatura: number;
  umidadeAr: number;
  diasSemRegar: number;
  tipoSolo: "arenoso" | "argiloso" | "misto";
};

export type ResultadoIrrigacao = {
  irrigar: boolean;
  nivel: "Baixa" | "Média" | "Alta";
  cor: string;
  mensagem: string;
};

export function calcularIrrigacao(
  dados: DadosIrrigacao
): ResultadoIrrigacao {
  let score = 0;

  if (dados.temperatura > 30) score += 2;
  else if (dados.temperatura > 25) score += 1;

  if (dados.umidadeAr < 40) score += 2;
  else if (dados.umidadeAr < 60) score += 1;

  if (dados.diasSemRegar >= 3) score += 2;
  else if (dados.diasSemRegar >= 2) score += 1;

  if (dados.tipoSolo === "arenoso") score += 1;

  if (score >= 5) {
    return {
      irrigar: true,
      nivel: "Alta",
      cor: "#E53935",
      mensagem: "Risco alto de solo seco. Irrigação recomendada.",
    };
  }

  if (score >= 3) {
    return {
      irrigar: true,
      nivel: "Média",
      cor: "#FB8C00",
      mensagem: "Clima quente detectado. Monitoramento recomendado.",
    };
  }

  return {
    irrigar: false,
    nivel: "Baixa",
    cor: "#43A047",
    mensagem: "Solo em condição estável.",
  };
}
