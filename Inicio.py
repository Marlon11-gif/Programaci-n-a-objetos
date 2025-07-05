import customtkinter
from tkinter import messagebox
from PIL import Image

# Configuración inicial
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("400x400")
root.title("Sistema de Inicio de Sesión")

# Cargar imagen de logo
imagen_logo = customtkinter.CTkImage(Image.open("clamatin.jpg"), size=(200, 200))
label_logo = customtkinter.CTkLabel(master=root, image=imagen_logo, text="")
label_logo.pack(pady=10)

# Diccionario para guardar usuarios en memoria
usuarios_registrados = {}

def mostrar_login():
    frame_registro.pack_forget()
    frame_login.pack(pady=20)

def mostrar_registro():
    frame_login.pack_forget()
    frame_registro.pack(pady=20)

def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def registrar_usuario():
    nuevo_usuario = entry_nuevo_usuario.get()
    nueva_contraseña = entry_nueva_contraseña.get()
    if nuevo_usuario and nueva_contraseña:
        if nuevo_usuario in usuarios_registrados:
            messagebox.showwarning("Atención", "El usuario ya existe")
        else:
            usuarios_registrados[nuevo_usuario] = nueva_contraseña
            messagebox.showinfo("Registro", "Usuario registrado correctamente")
            mostrar_login()
    else:
        messagebox.showwarning("Atención", "Por favor, completa todos los campos")

# Frame de Login
frame_login = customtkinter.CTkFrame(master=root)
label_login = customtkinter.CTkLabel(master=frame_login, text="Iniciar Sesión", font=("Arial", 20))
entry_usuario = customtkinter.CTkEntry(master=frame_login, placeholder_text="Usuario")
entry_contraseña = customtkinter.CTkEntry(master=frame_login, placeholder_text="Contraseña", show="*")

boton_login = customtkinter.CTkButton(
    master=frame_login, text="Iniciar Sesión", command=iniciar_sesion, fg_color="green"
)
boton_ir_a_registro = customtkinter.CTkButton(
    master=frame_login, text="¿No tienes cuenta? Regístrate", command=mostrar_registro, fg_color="green"
)

label_login.pack(pady=10)
entry_usuario.pack(pady=5)
entry_contraseña.pack(pady=5)
boton_login.pack(pady=10)
boton_ir_a_registro.pack()

# Frame de Registro
frame_registro = customtkinter.CTkFrame(master=root)
label_registro = customtkinter.CTkLabel(master=frame_registro, text="Registro de Usuario", font=("Arial", 20))
entry_nuevo_usuario = customtkinter.CTkEntry(master=frame_registro, placeholder_text="Nuevo Usuario")
entry_nueva_contraseña = customtkinter.CTkEntry(master=frame_registro, placeholder_text="Nueva Contraseña", show="*")

boton_registrar = customtkinter.CTkButton(
    master=frame_registro, text="Registrar", command=registrar_usuario, fg_color="red"
)
boton_ir_a_login = customtkinter.CTkButton(
    master=frame_registro, text="¿Ya tienes cuenta? Inicia sesión", command=mostrar_login, fg_color="red"
)

label_registro.pack(pady=10)
entry_nuevo_usuario.pack(pady=5)
entry_nueva_contraseña.pack(pady=5)
boton_registrar.pack(pady=10)
boton_ir_a_login.pack()

mostrar_login()

root.mainloop()