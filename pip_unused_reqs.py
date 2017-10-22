from __future__ import print_function
import pip
import pipdeptree
import subprocess

pkgs = pkgs = pip.get_installed_distributions()

dist_index = pipdeptree.build_dist_index(pkgs)
tree = pipdeptree.construct_tree(dist_index)

reversed_tree = pipdeptree.reverse_tree(tree)
names = [t.project_name for t, d in reversed_tree.items() if not d]

for name in names:
    try:
        result = subprocess.check_output(["rg", "-i", "-t", "py", name.replace('-', '_')])
    except subprocess.CalledProcessError as e:
        if not e.output:
            print(name)
