import random

waiter01_grammar = """
sentence => subject verb noun_phrase end
subject => 先生 | 小姐  | 小朋友 
noun_phrase =>  dout noun 
dout => 什么 | 哪种 | 哪个 
noun => 前菜 | 主菜 | 汤 | 甜点 | 酒水
verb => 喜欢 | 想要 | 需要
end => 呢？
"""


lajifenlei = """
sentence => subject verb noun end
subject =>  剩菜剩饭| 塑料瓶  | 金属 | 废旧电池 | 灯泡 | 过期药品 | 香蕉皮  
noun => 可回收垃圾 | 厨余垃圾 | 有害垃圾 | 其他垃圾 
verb => 是 | 属于 
end => 吗？
"""

def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip(): continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar


choice = random.choice

def generate(gram, target):
    if target not in gram: return target  # means target is a terminal expression

    expaned = [generate(gram, t) for t in choice(gram[target])]
    return ''.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])

generate(gram=create_grammar(waiter01_grammar), target='sentence')
generate(gram=create_grammar(lajifenlei), target='sentence')