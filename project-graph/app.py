from flask import Flask, request, render_template

app = Flask(__name__)

# Class Dijkstra
class Dijkstra:
    def __init__(self, simpul, graf):
        self.simpul = simpul
        self.graf = graf

    def mencari_rute(self, start, end):
        unvisited_simpul = {n: float('inf') for n in self.simpul}
        unvisited_simpul[start] = 0
        visited_simpul = {}
        parents = {}

        while unvisited_simpul:
            min_vertex = min(unvisited_simpul, key=unvisited_simpul.get)

            for neighbour in self.graf[min_vertex]:
                if neighbour in visited_simpul:
                    continue
                jalur_baru = unvisited_simpul[min_vertex] + self.graf[min_vertex].get(neighbour, float("inf"))
                if jalur_baru < unvisited_simpul[neighbour]:
                    unvisited_simpul[neighbour] = jalur_baru
                    parents[neighbour] = min_vertex

            visited_simpul[min_vertex] = unvisited_simpul[min_vertex]
            unvisited_simpul.pop(min_vertex)

            if min_vertex == end:
                break

        return parents, visited_simpul

    @staticmethod
    def jalur_dilewati(parents, start, end):
        jalur = [end]
        while True:
            key = parents[jalur[0]]
            jalur.insert(0, key)
            if key == start:
                break
        return jalur

# List simpul dan jaraknya dalam km
input_simpul = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'BB', 'CC', 'DD', 'EE',
                'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR',
                'SS', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ', 'AAA', 'BBB', 'CCC', 'DDD', 'EEE',
                'FFF', 'GGG', 'HHH', 'III', 'JJJ')
input_graf = {'A': {'B': 0.452},
              'B': {'A': 0.452, 'C': 0.261, 'G': 0.417},
              'C': {'B': 0.261, 'D': 0.311, 'F': 0.412},
              'D': {'C': 0.311, 'E': 0.412},
              'E': {'D': 0.412, 'F': 0.304, 'H': 0.523},
              'F': {'C': 0.412, 'E': 0.304, 'G': 0.267},
              'G': {'B': 0.418, 'F': 0.267, 'I': 0.515},
              'H': {'E': 0.523, 'I': 0.587, 'J': 0.180},
              'I': {'G': 0.515, 'H': 0.587, 'K': 0.190},
              'J': {'H': 0.180, 'K': 0.580, 'I': 0.175},
              'K': {'I': 0.190, 'J': 0.580, 'M': 0.166},
              'L': {'J': 0.175, 'M': 0.591, 'N': 0.060},
              'M': {'K': 0.166, 'L': 0.591, 'O': 0.060},
              'N': {'L': 0.060, 'O': 0.585, 'P': 0.110},
              'O': {'M': 0.060, 'N': 0.585, 'Q': 0.057},
              'P': {'N': 0.110, 'Q': 0.585, 'R': 0.142},
              'Q': {'O': 0.057, 'P': 0.585, 'S': 0.142},
              'R': {'P': 0.142, 'S': 0.587, 'T': 0.154},
              'S': {'Q': 0.142, 'R': 0.587, 'U': 0.141},
              'T': {'R': 0.154, 'U': 0.587, 'V': 0.052},
              'U': {'S': 0.141, 'T': 0.587, 'W': 0.065},
              'V': {'T': 0.052, 'W': 0.574, 'X': 0.219},
              'W': {'U': 0.065, 'V': 0.574, 'Y': 0.165},
              'X': {'V': 0.219, 'Y': 0.580, 'CC': 0.924},
              'Y': {'W': 0.165, 'X': 0.580},
              'Z': {'H': 1.600, 'AA': 0.486, 'BB': 0.661},
              'AA': {'Z': 0.486, 'BB': 0.439, 'FF': 0.500},
              'BB': {'Z': 0.661, 'AA': 0.439, 'EE': 0.955},
              'CC': {'X': 0.924, 'DD': 0.208},
              'DD': {'CC': 0.208, 'EE': 0.671},
              'EE': {'DD': 0.671, 'BB': 0.955, 'OO': 1.800},
              'FF': {'AA': 0.500, 'GG': 0.369},
              'GG': {'FF': 0.369, 'HH': 0.316},
              'HH': {'GG': 0.316, 'II': 0.347},
              'II': {'HH': 0.347, 'JJ': 0.181},
              'JJ': {'II': 0.181, 'KK': 0.331},
              'KK': {'JJ': 0.331, 'LL': 0.807},
              'LL': {'KK': 0.807, 'MM': 0.312, 'RR': 0.867},
              'MM': {'LL': 0.312, 'NN': 0.410},
              'NN': {'MM': 0.410, 'OO': 1.200},
              'OO': {'EE': 1.800, 'NN': 1.200, 'PP': 0.837},
              'PP': {'OO': 0.837, 'QQ': 0.636},
              'QQ': {'PP': 0.636, 'CCC': 0.593},
              'RR': {'LL': 0.867, 'SS': 0.914, 'WW': 0.660},
              'SS': {'RR': 0.914, 'TT': 1.000, 'VV': 0.562},
              'TT': {'SS': 1.000, 'UU': 0.634},
              'UU': {'TT': 0.634, 'VV': 1.300, 'XX': 0.172},
              'VV': {'SS': 0.562, 'UU': 1.300, 'WW': 0.881, 'AAA': 0.874},
              'WW': {'RR': 0.660, 'VV': 0.881, 'BBB': 0.849},
              'XX': {'UU': 0.172, 'YY': 1.700, 'ZZ': 0.812},
              'YY': {'XX': 1.700, 'GGG': 1.700},
              'ZZ': {'XX': 0.812, 'AAA': 1.070, 'EEE': 1.060},
              'AAA': {'VV': 0.874, 'ZZ': 1.070, 'BBB': 0.886},
              'BBB': {'WW': 0.849, 'CCC': 0.548},
              'CCC': {'QQ': 0.593, 'BBB': 0.548, 'DDD': 0.526},
              'DDD': {'CCC': 0.526, 'EEE': 2.000},
              'EEE': {'ZZ': 1.060, 'DDD': 2.000, 'FFF': 0.854},
              'FFF': {'EEE': 0.854, 'GGG': 1.200},
              'GGG': {'YY': 1.700, 'FFF': 1.200, 'HHH': 1.100},
              'HHH': {'GGG': 1.100, 'III': 1.900},
              'III': {'HHH': 1.900, 'JJJ': 0.207},
              'JJJ': {'III': 0.207}}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    start = request.form['start']
    end = request.form['end']
    if start not in input_simpul or end not in input_simpul:
        return "Simpul tidak valid. Pastikan simpul yang dimasukkan ada di dalam graf."
    dijkstra = Dijkstra(input_simpul, input_graf)
    parents, visited_simpul = dijkstra.mencari_rute(start, end)
    jalur = dijkstra.jalur_dilewati(parents, start, end)
    return render_template('result.html', jalur='->'.join(jalur), bobot=visited_simpul[end])

if __name__ == '__main__':
    app.run(debug=True)
