import psycopg2
from colorama import Fore


def print_error(message: str) -> None:
    print(Fore.LIGHTRED_EX + message + Fore.RESET)


def print_success(message: str) -> None:
    print(Fore.LIGHTGREEN_EX + message + Fore.RESET)


host = 'localhost'
port = 5432
dbname = 'postgres'
user = 'postgres'
password = 2508


def check_data():
    """ Check database connection """
    try:
        conn = psycopg2.connect(host=host,
                                port=port,
                                dbname=dbname,
                                user=user,
                                password=password)
    except psycopg2.Error:
        print_error('Unable to connect to database')  # proyekt to'xtab qolmasligi uchun raise ishlatmadim

    else:
        cur = conn.cursor()
        return cur


def create_table_products():
    cur = check_data()
    if cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS %s(
        id serial PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        image VARCHAR(255) NOT NULL,
        is_liked BOOLEAN NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """)
        cur.connection.commit()
        cur.close()
        print_success("Table created successfully")


def insert_data():
    cur = check_data()
    if cur:
        name = input(Fore.LIGHTGREEN_EX +
                     'Input product name: ' + Fore.RESET)
        image = input(Fore.LIGHTGREEN_EX + 'Input product image: ' + Fore.RESET)
        is_liked = input(Fore.LIGHTGREEN_EX + 'is this product liked? 1/0 : ' + Fore.RESET)

        if (is_liked == '1' or is_liked == '0') and name and image:
            cur.execute("""INSERT INTO products(name, image, is_liked)
            VALUES(%s, %s, %s)
            """, (name, image, is_liked))
            cur.connection.commit()
            cur.close()
            print_success("Product inserted successfully")
        else:
            print_error('Invalid input, please try again')


def delete_data():
    cur = check_data()
    if cur:
        _id = int(input(Fore.LIGHTGREEN_EX + 'Input product id to delete: '
                                             '' + Fore.RESET))
        cur.execute("""select * from products where id = %s""", (_id,))
        data = cur.fetchone()
        if data:
            cur.execute(""" DELETE FROM products
            where id = %s;""", (_id,)
                        )
            cur.connection.commit()
            cur.close()
            print_success('Product deleted successfully')
        else:
            print_error('Product not found')


def update_data():
    cur = check_data()
    if cur:
        try:
            _id = int(input(Fore.LIGHTGREEN_EX + 'Input product id to update: ' + Fore.RESET))
            cur.execute(""" select * from products where id = %s """, (_id,))
            data = cur.fetchall()
        except TypeError:
            print_error("please enter valid input")
        except ValueError:
            print_error("please enter valid input")
        else:
            if data:
                print(data)
                choice = input(Fore.LIGHTCYAN_EX + 'Would you like to update it? \nname => 1\nimage => '
                                                   '2\nis_liked =>'
                                                   '3\nexit => 0: ' + Fore.RESET)
                if choice == '1':
                    name = input(Fore.LIGHTGREEN_EX + 'Input products new name: ' + Fore.RESET)
                    cur.execute(""" UPDATE products set name = %s where id = %s""", (name, _id))
                    cur.connection.commit()
                elif choice == '2':
                    image = input(Fore.LIGHTGREEN_EX + 'Input products new image: ' + Fore.RESET)
                    cur.execute("""UPDATE products set image = %s where id = %s """, (image, _id))
                    cur.connection.commit()
                elif choice == '3':
                    is_liked = input(Fore.LIGHTGREEN_EX + 'Is this product liked? 1/0 : ' + Fore.RESET)
                    if is_liked == '1' or is_liked == '0':
                        cur.execute("""UPDATE products set is_liker = %s where id = %s""", (is_liked, _id))
                        cur.connection.commit()
                    else:
                        print_error('Invalid input, please try again')
                elif choice == '0':
                    return Fore.LIGHTGREEN_EX + 'Thank you for using this program' + Fore.RESET
                else:
                    print_error('Invalid input, please try again')
            else:
                print_error('Product not found')


def show_products():
    cur = check_data()
    if cur:
        cur.execute(""" SELECT * FROM products """)
        data = cur.fetchall()
        for row in data:
            print(row)
