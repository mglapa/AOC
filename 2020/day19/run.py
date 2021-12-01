
def parse():
    with open('input_ex.txt', 'r') as f:
        lines = f.read().split('\n\n')

    rules, message = lines
    rules = rules.split('\n')
    message = message.split('\n')
    
    # Parse rules into dict
    rule_dict = {}
    for r in rules:
        r = r.split(':')
        idx = r[0]
        rule = r[1].replace(' ', '').replace('"', '').split('|')
        rule_dict[idx] = rule
    
    return rule_dict, message

def check_rules():


def part1(rules, message):
    for m in message:
        check_rules(m, rules)



rules, message = parse()

part1(rules, message)


