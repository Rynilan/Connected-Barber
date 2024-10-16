from connect import *


class conexao():

    def salvar(self,pais,estado,cidade,cep,complemento,barbearia):
        try:
            sql = "INSERT INTO endereco (pais,estado,cidade,cep,complemento,barbearia) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (pais,estado,cidade,cep,complemento,barbearia)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "Endereço cadastrado com sucesso!")

        except:
            print("Erro ao adicionar o Endereço")

    def lista():
        try:

            mycursor.execute("SELECT * FROM endereco")

            myresult = mycursor.fetchall()

            for x in myresult:
              print(x)
              
        except:
            print("Erro ao conectar a tabela")

    def apagar(id):

        try:
            sql = "DELETE FROM endereco WHERE id = %s"
            mycursor.execute(sql, (id,))
            mydb.commit()

        except:
            print("Erro ao deletar o endereço da barbearia")

    def alterar(id):
        escolha = input("Que campo você deseja mudar? (pais,estado,cidade,cep,complemento,barbearia): ")
        
        if escolha == "pais":
            novo_pais = int (input("Alterar o Pais para: "))
            
            try:
                sql = "UPDATE endereco SET pais = %s WHERE id = %s"
                mycursor.execute(sql, (novo_pais, id))
                mydb.commit()
                print(mycursor.rowcount, "Pais alterado com sucesso!")
            except:
                print("Erro ao mudar o pais")


        elif escolha == "estado":
            novo_estado = int (input("Alterar o Estado para: "))

            try:
                sql = "UPDATE endereco SET estado = %s WHERE id = %s"
                mycursor.execute(sql, (novo_estado, id))
                mydb.commit()
                print(mycursor.rowcount, "Estado alterado com sucesso")
            except:
                print("Erro ao mudar o estado")

        elif escolha == "cidade":
            nova_cidade = int (input("Alterar o cidade para: "))

            try:
                sql = "UPDATE endereco SET cidade = %s WHERE id = %s"
                mycursor.execute(sql, (nova_cidade, id))
                mydb.commit()
                print(mycursor.rowcount, "Cidade alterado com sucesso")
            except:
                print("Erro ao mudar a Cidade")

        elif escolha == "cep":
            novo_cep = input("Alterar o Cep para: ")

            try:
                sql = "UPDATE endereco SET cep = %s WHERE id = %s"
                mycursor.execute(sql, (novo_cep, id))
                mydb.commit()
                print(mycursor.rowcount, "Cep alterado com sucesso")
            except:
                print("Erro ao mudar o Cep")
        
        elif escolha == "complemento":
            novo_complemento = input("Alterar o Cep para: ")

            try:
                sql = "UPDATE complemento SET cep = %s WHERE id = %s"
                mycursor.execute(sql, (novo_complemento, id))
                mydb.commit()
                print(mycursor.rowcount, "Complemento alterado com sucesso")
            except:
                print("Erro ao mudar o Complemento")
        
        

mycursor.close()
mydb.close()

