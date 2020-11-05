from argparse import ArgumentParser

from utils.utils import run_all_scripts


def main():
    parser = ArgumentParser(description='Run all migration scripts.')
    # parser.add_argument('migrations_dir', help='Directory with the migrations')
    # parser.add_argument('config', help='Service config file')
    # parser.add_argument('secrets', help='Service database admin secrets')

    args = parser.parse_args()
    run_all_scripts("/home/felipe/Documents/insper/megadados/Megadados2020-2-Projeto1-alunos/tasklist/database/migrations", "/home/felipe/Documents/insper/megadados/Megadados2020-2-Projeto1-alunos/tasklist/config/config.json", "/home/felipe/Documents/insper/megadados/Megadados2020-2-Projeto1-alunos/tasklist/config/db_admin_secrets.json")

    # python3 run_all_migrations /home/felipe/Documents/insper/megadados/Megadados2020-2-Projeto1-alunos/tasklist/database/migrations  /home/felipe/Documents/insper/megadados/Megadados2020-2-Projeto1-alunos/tasklist/config/config.json /home/felipe/Documents/insper/megadados/Megadados2020-2-Projeto1-alunos/tasklist/config/db_admin_secrets.json


if __name__ == '__main__':
    main()
