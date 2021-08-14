# !/usr/bin/python3
# encoding: ISO-8859-1
"""Módulo criado para realizar o processo de criação de ambiente de desenvolvimento."""

import os
import sys
import subprocess


LISTA_PKGS = ["flake8", "pylint", "black", "mypy", "pydocstyle", "pytest", "pre-commit"]


def extrai_caminho_projeto(*args: str) -> str:
    """
    Coleta o caminho para realizar os processos de criação do ambiente.

    Parameter
    Return
        :return: Caminho e Nome do projeto
        :rtype: str, str

    Exemple
        >>> path = "/home/dev/DevProjects/pydenv/"
        >>> extrai_caminho_projeto(path)
        "/home/dev/DevProjects"

    """
    if args is not None:
        caminho_projeto: str = os.getcwd()
        return caminho_projeto


def extrai_nome_projeto(*args: str) -> str:
    """
    Coleta o nome do projeto com base os.path.

    Parameter
        :param args: Caminho do projeto
        :type args: str

    Return
        :return: Nome Projeto
        :rtype: str

    Exemple
        >>> path = "/home/dev/DevProjects/pydenv/"
        >>> extrai_nome_projeto(path)
        "pydenv"

    """
    if args is not None:
        nome_projeto: str = os.path.basename(extrai_caminho_projeto())
        return nome_projeto


def check_python_version(*args: str) -> int:
    """
    Coleta o nome do projeto com base os.path.

    Parameter
        :param args: Versão do Python
        :type args: str

    Return
        :return: Versão do Python
        :rtype: int

    Exemple
        >>> path = "/home/dev/DevProjects/pydenv/"
        >>> extrai_nome_projeto(path)
        "pydenv"

    """
    if args is not None:
        python_version: str = sys.version.split(" ")[0].split(".")[0]
        if python_version == '3':
            return int(python_version)


def create_virtual_env(nome_projeto: str = extrai_nome_projeto()):
    subprocess.check_call([sys.executable, '-m', 'venv', f'.{nome_projeto}'])

def install_pkgs_pip():
    for pkg in LISTA_PKGS:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])
