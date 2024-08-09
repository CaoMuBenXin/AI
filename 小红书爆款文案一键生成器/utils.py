# 与ai交互
from prompt_template import user_template_txt, system_template_txt
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from xiaohongshu_model import Xiaohongshu


def generate_xiaohongshu(subject, api_key="sk-aBVw9wETZ1mYSbn20a35E587580c437dB0BdA47792292d14"):
    """
    与AI交互，返回包含标题和正文的Xiaohongshu类对象
    :param subject: 主题
    :param api_key: 密钥
    :return: Xiaohongshu类对象
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_txt),
        ("user", user_template_txt)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key, base_url="https://xiaoai.plus/v1")
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    # 得到Xiaohongshu类的对象
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "subject": subject
    })

    return result


if __name__ == '__main__':
    print(generate_xiaohongshu(subject="蔡徐坤的梗"))
