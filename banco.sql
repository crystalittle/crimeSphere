-- Criação do banco de dados
CREATE DATABASE crime_sphere;

-- Selecionando o banco de dados
USE crime_sphere;

-- Tabela de Usuários
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Casos Criminais
CREATE TABLE cases (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  image_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Comentários
CREATE TABLE comments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  case_id INT,
  user_id INT,
  comment TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (case_id) REFERENCES cases(id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
