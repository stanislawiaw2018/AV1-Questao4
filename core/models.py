from django.db import models
class Amigo(models.Model):
    class Meta:
        verbose_name = "Amigo"
        verbose_name_plural = "Amigos"
    choice_amigo = [
        ("esc","Escola"),
        ("pre","Prédio")
    ]
    nome = models.CharField("Nome",max_length=50, null=False,blank=False)
    nome_mae = models.CharField("Nome da Mãe", max_length=50,null=False,blank=False)
    telefone = models.CharField("Telefone",max_length=12,null=False,blank=False)
    grupo_amgigo = models.CharField("Grupo Amigo",max_length=3,choices=choice_amigo,default='esc',null=False,blank=False)

    def __str__(self):
        return self.nome

class Revista(models.Model):
    class Meta:
        verbose_name = "Revista"
        verbose_name_plural = "Revistas"
    numero_edicao = models.IntegerField("Número da Edição",null=False,blank=False)
    ano = models.IntegerField("Ano",null=False,blank=False)

    def __str__(self):
        return self.numero_edicao

class Emprestimo(models.Model):
    class Meta:
        verbose_name_plural = "Emprestimos"

    amigo = models.ForeignKey(Amigo,on_delete=models.CASCADE,null=True,blank=True)
    revista = models.ForeignKey( Revista,on_delete=models.CASCADE,null=True,blank=True)
    data_emprestimo = models.DateField("Data Emprestimo",null=False,blank=False)
    data_devolucao = models.DateField("Data Devolucao",null=False,blank=False)

    def __str__(self):
        return self.amigo

class Caixa(models.Model):
    class Meta:
        verbose_name_plural = "Caixas"

    numero = models.IntegerField("Número da Caixa",null=False,blank=False)
    etiqueta = models.CharField("Etiqueta",max_length=20,null=False,blank=False)
    cor = models.CharField("Cor da Caixa", max_length=20,null=False,blank=False)
    revista = models.ForeignKey( Revista,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.numero
class Colecao(models.Model):
    class Meta:
        verbose_name_plural = "Coleções"
        verbose_name = "Coleção"
    nome = models.CharField("Nome da Coleção", max_length=20, null=False,blank=False)
    revista = models.ForeignKey(Revista,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.nome


