import { useEffect, useState } from "react";
import {
  calcularIrrigacao,
  DadosIrrigacao,
  ResultadoIrrigacao,
} from "../services/irrigacaoService";

export function useIrrigacao(dados: DadosIrrigacao) {
  const [resultado, setResultado] =
    useState<ResultadoIrrigacao | null>(null);

  useEffect(() => {
    const decisao = calcularIrrigacao(dados);
    setResultado(decisao);
  }, [dados]);

  return resultado;
}
