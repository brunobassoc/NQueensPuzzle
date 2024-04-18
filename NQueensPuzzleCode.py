import time

class Solucao:
    def isSafe1(self, row, col, board, n):
        duprow = row
        dupcol = col

        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1

        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1

        row = duprow
        col = dupcol
		
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        return True

    def resolve(self, col, board, ans, n):
        if col == n:
            ans.append(list(board))
            return

        for row in range(n):
            if self.isSafe1(row, col, board, n):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.resolve(col+1, board, ans, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    def resolveNQueens(self, n):
        ans = []
        board = ['.'*n for _ in range(n)]
        self.resolve(0, board, ans, n)
        return ans

n = int(input('Insira o valor de rainhas aqui:'))
tempo_inicial = time.time()
aux = Solucao()
resultado = aux.resolveNQueens(n)
tempo_final = time.time()
for i in range(len(resultado)):
    solucoes = (i+1)

print(f"Quantidade de soluções: {solucoes}")
print(f"Tempo de execução: {tempo_final - tempo_inicial}")