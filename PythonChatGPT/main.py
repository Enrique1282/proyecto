import openai
import config
import typer
from rich import print
from rich.table import Table


def main():

    openai.api_key = config.api_key

    print("[bold green]ChatGPT API en Pythjon[/bold green]")

    table = Table("Comando", "Descripcion")
    table.add_row("exit", "salir de la aplicacion")
    table.add_row("new", "Crear una nueva conversación")
    print(table)

    # Este es el contexto del asistente, le pones lo que quieras y ya esta. 
    context = {"role": "system", "content": "Eres un asistente muy util"}

    messages=[context]

    while True:

        content = __prompt()
    
        if content == "new":
            print("Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        respuesta_content = respuesta.choices[0].message.content

        messages.append({"role": "assistant", "content": respuesta_content})
    
        print(f"[bold green]> [/bold green] [green]{respuesta_content}[/green]")

def __prompt() -> str:
    
    prompt = typer.prompt("\n¿Sobre que quieres hablar? ")
    
    if prompt =="exit":
       exit = typer.confirm("¿Estas seguro seguro seguro ji jo juu???")
       if exit:
           print("¡ Hasta luego!")
           raise typer.Abort()
        
       return __prompt()
    
    return prompt

if __name__== "__main__":
    typer.run(main)