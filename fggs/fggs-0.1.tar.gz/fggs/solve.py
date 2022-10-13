import torch


def check_args(a, b):
    if not 1 <= b.ndim <= 2:
        raise ValueError(f'b must have 1 or 2 dimensions (not {b.ndim})')
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError(f'a must be a square matrix (not {a.shape})')
    if a.shape[0] != b.shape[0]:
        raise ValueError(f'b must have the same number of rows as a (a has {a.shape[0]}, b has {b.shape[0]})')
    return a.shape[0]


def swap(x, y):
    t = x.clone()
    x.copy_(y)
    y.copy_(t)

    
def solve_utril_(l, b):
    """Solve l @ x = b by forward substitution, where l is unit lower triangular.
    If l is in fact not unit lower triangular, the elements above the
    diagonal are treated as 0 and the elements on the diagonal are treated as 1.

    Result:
    The solution is written to b.

    Golub and van Loan, 3rd ed., Algorithm 3.1.1 (p. 89)
    """
    n = check_args(l, b)
    for i in range(1, n):
        b[i] -= l[i,:i] @ b[:i]

        
def solve_triu_(u, b):
    """Solve u @ x = b by backward substitution, where u is upper triangular.
    If u is in fact not upper triangular, the elements below the
    diagonal are treated as 0.

    Result:
    The solution is written to b.

    Golub and van Loan, 3rd ed., Algorithm 3.1.2 (p. 89)
    """
    n = check_args(u, b)
    if n > 0:
        b[n-1] /= u[n-1, n-1]
        for i in range(n-2, -1, -1):
            b[i] -= u[i,i+1:] @ b[i+1:]
            b[i] /= u[i, i]

            
def lu_(a, b, cols=None):
    """If A is an n x n matrix, b is an n x r matrix, and cols=(j0, j1)
    is a range of columns of A, find P, L, and U such that:
    
    - P is an n x n permutation matrix
    - L is an (n-j0) x (j1-j0) lower unit triangular matrix
    - U is a (j1-j0) x (j1-j0) upper triangular matrix
    - PA[j0:n,j0:j1] = LU

    Result:
    - L sans its diagonal is written to the lower triangle of A[j0:n,j0:j1]
    - U is written to the upper triangle of A[j0:j1,j0:j1]
    - PA is written to the rest of A
    - Pb is written to b

    Golub and van Loan, 3rd ed., Algorithm 3.4.1 (p. 112)

    """

    n = check_args(a, b)
    if cols is None:
        j0, j1 = 0, n
    else:
        j0, j1 = cols
        j1 = min(j1, n)
    
    for k in range(j0, j1):
        mu = torch.argmax(torch.abs(a[k:,k]))+k
        swap(a[k], a[mu])
        swap(b[k], b[mu])
        if a[k,k] != 0.:
            a[k+1:,k] /= a[k,k]
            a[k+1:,k+1:j1] -= torch.outer(a[k+1:,k], a[k,k+1:j1])


def solve(a, b, block_size):
    """Solve a @ x = b by block Gaussian elimination with partial pivoting.

    Golub and van Loan, 3rd ed., Section 3.4.7 (p. 116)
    """

    n = check_args(a, b)
    a = a.clone()
    b = b.clone()
    r = block_size
    for k in range(0, n, r):
        lu_(a, b, cols=(k,k+r))
        l11 = a[k:k+r,k:k+r]
        l21 = a[k+r:,k:k+r]
        u12 = a[k:k+r,k+r:]
        solve_utril_(l11, u12)
        a[k+r:,k+r:] -= l21 @ u12

    solve_utril_(a, b)
    solve_triu_(a, b)
    return b

if __name__ == "__main__":
    import timeit

    n = 10
    torch.set_default_dtype(torch.double)
    tol = 1e-3
    
    for i in range(100):
        l = torch.randn(n, n).tril(-1) + torch.eye(n)
        b = torch.randn(n)
        x = b.clone()
        solve_utril_(l, x)
        assert (torch.norm(l @ x - b) < tol), (l @ x, b)
    print('passed')
    
    for i in range(100):
        l = torch.randn(n, n).tril(-1) + torch.eye(n)
        b = torch.randn(n, 2)
        x = b.clone()
        solve_utril_(l, x)
        assert (torch.norm(l @ x - b) < tol), (l @ x, b)
    print('passed')

    for i in range(100):
        u = torch.randn(n, n).triu()
        b = torch.randn(n) 
        x = b.clone()
        solve_triu_(u, x)
        assert (torch.norm(u @ x - b) < tol), (u @ x, b)
    print('passed')
    
    for i in range(100):
        u = torch.randn(n, n).triu()
        b = torch.randn(n, 2)
        x = b.clone()
        solve_triu_(u, x)
        assert (torch.norm(u @ x - b) < tol), (u @ x, b)
    print('passed')

    for i in range(100):
        a = torch.randn(n, n)
        b = torch.randn(n)
        a1 = a.clone()
        b1 = b.clone()
        lu_(a1, b1)
        a2 = a1.tril(-1) @ a1.triu() + a1.triu()
        assert (torch.norm(torch.linalg.solve(a, b) - torch.linalg.solve(a2, b1)) < tol)
    print('passed')
    
    for i in range(100):
        a = torch.randn(n, n)
        b = torch.randn(n)
        x = solve(a, b, 3)
        assert (torch.norm(a @ x - b) < tol), (a @ x, b)
    print('passed')
    
    for i in range(100):
        a = torch.randn(n, n)
        b = torch.randn(n, 2)
        x = solve(a, b, 3)
        assert (torch.norm(a @ x - b) < tol), (a @ x, b)
    print('passed')

    for n in [100, 1000]:
        for p in [100, 1000]:
            for r in [1, 10, 100, 1000]:
                def solve1():
                    a = torch.randn(n, n)
                    b = torch.randn(n, p)
                    x = torch.linalg.solve(a, b)
                def solve2():
                    a = torch.randn(n, n)
                    b = torch.randn(n, p)
                    x = solve(a, b, r)

                #t1 = timeit.timeit(solve1, number=10)
                t2 = timeit.timeit(solve2, number=10)
                #print(f'rows={n} cols={p} block_size={r} theirs={t1} ours={t2} ratio={t2/t1}')
