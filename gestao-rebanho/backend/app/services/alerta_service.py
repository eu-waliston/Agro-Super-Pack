from datetime import date, timedelta
from app.models.aplicacao_vacina import AplicarVacina
from app.models.alerta import Alerta
from app.models.registro_peso import RegistroPeso

def verificar_vacinas(db):
    
    hoje = date.today()
    sete_dias = hoje + timedelta(days=7)
    
    aplicacoes = db.query(AplicarVacina).all()
    
    for aplicacao in aplicacoes:
        
        if aplicacao.proxima_dose < hoje:
            alerta = Alerta(
                animal_id=aplicacao.animal_id,
                tipo="vacina_vencida",
                nivel="critical",
                mensagem="Vacina vencida. Aplicação urgente necessária"
            )
            db.add(alerta)
            
        elif aplicacao.proxima_dose <= sete_dias:
            alerta = Alerta(
                animal_id=aplicacao.animal_id,
                tipo="vacina_proxima",
                nivel="warning",
                mensagem="Vacina poróxima de Vencimento"
            )
            db.add(alerta) 
    db.commit()

def verificar_peso(db):
    
    animais = db.query(RegistroPeso.animal_id).distinct().all()
    
    for (animal_id,) in animais:
        
        registros = (
            db.query(RegistroPeso)
                .filter(RegistroPeso.animal_id == animal_id)
                .order_by(RegistroPeso.data_registro.desc())
                .limit(2)
                .all()
        )
        
        if len(registros) == 2:
            if registros[0].peso < registros[1].peso:
                alerta = Alerta (
                    animal_id=animal_id,
                    tipo="queda_peso",
                    nivel="warning",
                    mensagem="Animal apresentou queda de peso."
                )
                db.add(alerta)
    db.commit()
    
