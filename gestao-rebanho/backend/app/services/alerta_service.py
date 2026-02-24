from datetime import date, timedelta, datetime
from app.models.aplicacao_vacina import AplicarVacina
from app.models.alerta import Alerta
from app.models.registro_peso import RegistroPeso

from sqlalchemy.orm import Session
from app.models.vacina import Vacina

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
    
def criar_alerta_se_nao_existir(
    db: Session,
    animal_id: int,
    tipo: str,
    mensagem: str,
    nivel: str = "MODERADO"
) :
    alerta_existente = db.query(Alerta).filter(
        Alerta.animal_id == animal_id,
        Alerta.tipo == tipo,
        Alerta.resolvido == False
    ).first()
    
    if alerta_existente:
        return
    
    novo_alerta = Alerta(
        animal_id=animal_id,
        tipo=tipo,
        mensagem=mensagem,
        nivel=nivel,
        craido_em=datetime.utcnow()
    )
    
    db.add(novo_alerta)
    db.commit()

def processar_alertas(db: Session):
    hoje = datetime.utcnow().date()    
    vacinas = db.query(Vacina).all()
    
    for vacina in vacinas:
        if vacina.data_proxima_dose and vacina.data_proxima_dose < hoje:
            criar_alerta_se_nao_existir(
                db=db,
                animal_id=vacina.animal_id,
                tipo="VACINA_VENCIDA",
                mensagem="Vacina vencida",
                nivel="CRITICO"
            )
            
            
