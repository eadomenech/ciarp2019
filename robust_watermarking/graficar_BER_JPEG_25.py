# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-


def run_main():
    db_images = [
        'csg562-003', 'csg562-004', 'csg562-005', 'csg562-006',
        'csg562-007', 'csg562-008', 'csg562-009', 'csg562-010',
        'csg562-011', 'csg562-012', 'csg562-013', 'csg562-014',
        'csg562-015', 'csg562-016', 'csg562-017', 'csg562-018',
        'csg562-019', 'csg562-020', 'csg562-021', 'csg562-022',
        'csg562-023', 'csg562-024', 'csg562-025', 'csg562-026',
        'csg562-027', 'csg562-028', 'csg562-029', 'csg562-030',
        'csg562-031', 'csg562-032', 'csg562-033', 'csg562-034',
        'csg562-035', 'csg562-036', 'csg562-037', 'csg562-038',
        'csg562-039', 'csg562-040', 'csg562-041', 'csg562-042',
        'csg562-043', 'csg562-044', 'csg562-045', 'csg562-046',
        'csg562-047', 'csg562-048', 'csg562-049', 'csg562-050',
        'csg562-054', 'csg562-055', 'csg562-056', 'csg562-057',
        'csg562-058', 'csg562-059', 'csg562-060', 'csg562-061',
        'csg562-062', 'csg562-063', 'csg562-064', 'csg562-065'
    ]
    import matplotlib.pyplot as plt
    #plt.title('BER from extracted watermark images QF = 25%')
    images = []
    for i in range(60):
        images.append(i+1)
    plt.plot(
        images,
        [
            0.000000,0.001041,0.001041,0.003122,0.002081,0.000000,0.005203,0.003122,0.000000,0.001041,0.001041,0.001041,0.000000,0.000000,0.000000,0.000000,0.000000,0.001041,0.000000,0.001041,0.003122,0.000000,0.001041,0.002081,0.001041,0.000000,0.000000,0.001041,0.000000,0.001041,0.001041,0.001041,0.000000,0.000000,0.001041,0.001041,0.000000,0.001041,0.001041,0.002081,0.000000,0.002081,0.002081,0.000000,0.000000,0.002081,0.001041,0.002081,0.003122,0.000000,0.002081,0.000000,0.001041,0.004162,0.002081,0.000000,0.002081,0.000000,0.000000,0.003122
        ], '^', label='(Avila-Domenech, 2018)', markersize=16)
    plt.plot(
        images,
        [
            0.001041,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.001041,0.001041,0.000000,0.001041,0.000000,0.002081,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.001041,0.000000,0.002081,0.000000,0.001041,0.001041,0.002081,0.002081,0.000000,0.000000,0.000000,0.001041,0.000000,0.000000,0.000000,0.000000,0.000000,0.003122,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.001041,0.000000,0.000000,0.000000,0.000000,0.001041,0.000000,0.001041,0.000000,0.000000,0.000000,0.001041,0.000000,0.000000
        ], 's', label='Proposed (robust only)', markersize=10, color='green')
    plt.plot(
        images,
        [
            0.001041,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.001041,0.002081,0.001041,0.001041,0.000000,0.001041,0.001041,0.000000,0.000000,0.000000,0.001041,0.000000,0.001041,0.000000,0.000000,0.000000,0.001041,0.001041,0.000000,0.000000,0.000000,0.001041,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.002081,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.001041,0.000000,0.002081,0.002081,0.000000,0.001041,0.001041,0.000000,0.001041,0.000000,0.000000,0.001041,0.000000,0.002081
        ], 'ro', label='Proposed (robust + fragile)', markersize=8, color='red')
    plt.ylabel('BER')
    plt.legend(loc='upper left', numpoints=1)
    plt.axis([0, 60, 0, 0.006])
    plt.xticks(images, db_images, size='small', color='k', rotation=-85)
    plt.grid(True)
    font = {
        'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 50}
    plt.rc('font', **font)
    plt.show()


if __name__ == "__main__":
    run_main()