class AlgumaCoisa:
    def __enter__(self, exc_type, exc_val, exc_tb):
        print('Esotu Entrando')
        print('Estou Saindo')
    
    with AlgumaCoisa() as ola:
        print('Estou no meio')
