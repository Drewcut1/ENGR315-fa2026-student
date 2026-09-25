import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    ### YOUR CODE HERE ###

    a = [1]
    b = [1/(math.sqrt(2))]
    t = [0.25]
    p = [1]
    error = 1
    n = 1

    while error >= target_error:

        n = n + 1
        for i in range(1, n):
            ### YOUR CODE HERE ###
            a.append((a[i-1] + b[i-1])/2)
            b.append(math.sqrt(a[i-1]*b[i-1]))
            p.append(p[i-1] * 2)
            t.append(t[i-1] - p[i-1]*math.pow(a[i]-a[i-1], 2))
            pi_estimate = math.pow(a[i] + b[i], 2)/(4*t[i])
            error = abs(pi_estimate - math.pi)

    return pi_estimate
    
    # change this so an actual value is returned

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
