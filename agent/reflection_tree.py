import csv

# Load TSV into dictionary
def load_tree(file_path):
    tree = {}
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            tree[row['id']] = row
    return tree

# Get next node based on parentId
def get_next_node(tree, current_id):
    for node in tree.values():
        if node['parentId'] == current_id:
            return node
    return None

# Parse decision logic
def evaluate_decision(node, answer):
    rules = node['options'].split(';')
    for rule in rules:
        condition, target = rule.split(':')
        values = condition.replace("answer=", "").split('|')
        if answer in values:
            return target
    return None

# Main runner
def run_tree(tree):
    current = tree['START']
    signals = {'axis1': [], 'axis2': [], 'axis3': []}

    while current:
        node_type = current['type']

        if node_type == 'start':
            print("\n" + current['text'])
            current = get_next_node(tree, current['id'])

        elif node_type == 'question':
            print("\n" + current['text'])
            options = current['options'].split('|')

            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")

            choice = int(input("Choose option: ")) - 1
            answer = options[choice]

            # store signal
            if current['signal']:
                axis, val = current['signal'].split(':')
                signals[axis].append(val)

            # go to next (decision or next node)
            next_node = get_next_node(tree, current['id'])
            current = next_node
            current['user_answer'] = answer

        elif node_type == 'decision':
            answer = current.get('user_answer')
            next_id = evaluate_decision(current, answer)
            current = tree[next_id]

        elif node_type == 'reflection':
            print("\n💡 " + current['text'])
            current = get_next_node(tree, current['id'])

        elif node_type == 'bridge':
            print("\n➡️ " + current['text'])
            current = tree[current['target']]

        elif node_type == 'summary':
            print("\n📊 Summary:")

            def dominant(axis):
                return max(set(signals[axis]), key=signals[axis].count) if signals[axis] else "neutral"

            print(f"Axis1 (Control): {dominant('axis1')}")
            print(f"Axis2 (Contribution): {dominant('axis2')}")
            print(f"Axis3 (Perspective): {dominant('axis3')}")

            current = get_next_node(tree, current['id'])

        elif node_type == 'end':
            print("\n" + current['text'])
            break

    print("\nDone.")

if __name__ == "__main__":
    # tree = load_tree("../tree/reflection-tree.tsv")
    tree = load_tree("tree/reflection-tree.tsv")
    run_tree(tree)