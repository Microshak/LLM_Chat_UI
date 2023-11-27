from flask import Flask, redirect, url_for, request, Blueprint

from flask import Blueprint
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from chat.common import common
from langchain.chains.summarize import load_summarize_chain
from chat import app
from langchain.chains.llm import LLMChain
common =  common()
llm = common.llm


sum = Blueprint('sum', __name__)


@sum.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    dat =  data
    msg = dat["txt"]
    id=dat["id"]
    chatNum = dat["chatNum"]
    
    prompt_template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""
    prompt = PromptTemplate.from_template(prompt_template)

    llm_chain = LLMChain(llm=llm, prompt=prompt)

    chain = load_summarize_chain(llm, chain_type="stuff")

    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
    output = stuff_chain.run({"text": msg}, tags=[id,chatNum])
    return ""

