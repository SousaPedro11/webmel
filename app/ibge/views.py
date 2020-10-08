import requests
from flask import render_template

from app.ibge import bp_ibge

data = requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/1994|1995|1996|1997|1998'
                    '|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015'
                    '|2016|2017|2018/variaveis/106|215|1000215?localidades=N1[all]|N3[11,12,13,14,15,16,17,'
                    '22]|N2[all]&classificacao=80[2687]', stream=True)
data = data.json()


@bp_ibge.route('/')
def index():
    return render_template("home.html")


@bp_ibge.route('/quantidade/')
def quantidade():
    index = 0
    pais = data_build(index, 'N1')
    regiao = data_build(index, 'N2')
    estado = data_build(index, 'N3')
    return render_template("quantidade.html", pais=pais, regiao=regiao, estado=estado)


@bp_ibge.route('/valor/')
def valor():
    index = 1
    pais = data_build(index, 'N1')
    regiao = data_build(index, 'N2')
    estado = data_build(index, 'N3')
    return render_template("valor.html", pais=pais, regiao=regiao, estado=estado)


@bp_ibge.route('/percentual/')
def percentual():
    index = 2
    pais = data_build(index, 'N1')
    regiao = data_build(index, 'N2')
    estado = data_build(index, 'N3')

    return render_template("percentual.html", pais=pais, regiao=regiao, estado=estado)


def data_build(index, lv):
    dado = {}
    dado_base = data[index]['resultados'][0]['series']
    for item in dado_base:
        localidade_base = item['localidade']
        if localidade_base['nivel']['id'] == lv:
            localidade = localidade_base['nome']
            dado[localidade] = item['serie']
    return dado
