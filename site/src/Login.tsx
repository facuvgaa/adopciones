import styled from "styled-components";
import { useState } from "react";
import axios from "axios";

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #1e1e1e;
  margin: 0;
  padding: 0;
  box-sizing: border-box;

  form {
    background: #292929;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
    max-width: 400px;
    width: 100%;
  }

  ul {
    list-style: none;
    padding: 0;
    margin-bottom: 1.5rem;
  }

  label {
    color: #cfcfcf;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
    display: block;
  }

  input {
    width: 100%;
    padding: 0.75rem;
    margin-top: 0.5rem;
    border: 1px solid #444;
    border-radius: 4px;
    font-size: 1rem;
    color: #fff;
    background-color: #333;
    box-sizing: border-box;
  }

  input:focus {
    outline: none;
    border-color: #007bff;
    background-color: #292929;
  }

  button {
    width: 100%;
    padding: 0.75rem;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: #0056b3;
    }
  }

  @media (max-width: 768px) {
    form {
      padding: 1.5rem;
    }

    input,
    button {
      font-size: 0.9rem;
    }
  }
`;

const Login = (): JSX.Element => {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // Evita que el formulario recargue la página.

    try {
      // Enviar solicitud al backend usando axios
      const response = await axios.post("http://localhost:8000/api/login/", {
        username: email, // Django usa `username` en lugar de `email`.
        password,
      });

      // Mostrar token o mensaje de éxito en la consola
      console.log("Respuesta del servidor:", response.data);

      // Aquí puedes guardar el token en localStorage o manejar el flujo del usuario
      alert("Inicio de sesión exitoso");
    } catch (error: any) {
      console.error("Error durante el inicio de sesión:", error.response?.data);
      alert("Credenciales inválidas. Intenta nuevamente.");
    }
  };

  return (
    <Container>
      <form onSubmit={handleSubmit}>
        <ul>
          <label htmlFor="email">Correo electrónico</label>
          <input
            id="email"
            type="email"
            placeholder="Ingresa tu correo"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </ul>
        <ul>
          <label htmlFor="password">Contraseña</label>
          <input
            id="password"
            type="password"
            placeholder="Ingresa tu contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </ul>
        <ul>
          <button type="submit">Ingresar</button>
        </ul>
      </form>
    </Container>
  );
};

export default Login;


