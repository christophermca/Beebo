from testground import main
from map_enviroment import create_map, set_item
_map = create_map(16, 16)
output = set_item(0, 0, 2, _map)

main()
