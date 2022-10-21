def so_coincidentes(m1, m2):
    mf = []

    for l in range(len(m1)):
        mf.append([])
        for c in range(len(m1[0])):
            mf[l].append(0)
        

    for il in range(len(m1)):
        for ic in range(len(m1[0])):
            if m1[il][ic] == m2[il][ic]:
                mf[il][ic] = m1[il][ic]

    return mf
