# main.py
import os
from core.brain import *
from core.planner import *
from core.multiagent import *
from memory.memory import *
from voice.voice import *
from automation.system import *
from evolution.evolve import *
from server.api import *

def load_env():
    """Cargar la API Key desde .env"""
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("Ingresa tu OPENAI_API_KEY: ")
    return api_key

def main():
    print("=== Ultron OS Iniciado ===")
    
    # Cargar API Key
    api_key = load_env()
    print("API Key cargada correctamente.")
    
    # Inicializar módulos
    print("Inicializando módulos...")
    brain = Brain(api_key)
    planner = Planner()
    agents = MultiAgentSystem()
    memory = Memory()
    voice = VoiceSystem()
    automation = AutomationSystem()
    evolution = Evolver()
    server = ServerAPI()
    
    print("Todos los módulos inicializados.")
    
    # Ejemplo simple de ejecución
    while True:
        try:
            command = input("\nComando para Ultron OS (escribe 'exit' para salir): ")
            if command.lower() == "exit":
                print("Apagando Ultron OS...")
                break
            response = brain.process(command)
            print(f"Ultron: {response}")
        except KeyboardInterrupt:
            print("\nInterrupción manual. Cerrando Ultron OS...")
            break

if __name__ == "__main__":
    main()
