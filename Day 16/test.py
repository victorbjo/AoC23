def getHashtags(lines, y, x, dy, dx):
    lines = copy.deepcopy(lines)
    beams = [(y, x, dy, dx)]
    seen, mirs = set(), set()
    while beams:
        i = beams.pop()
        curY, curX, dY, dX = i
        if i in seen:
            continue
        else:
            seen.add(i)
        if (
            0 <= curX < len(lines[0])
            and 0 <= curY < len(lines)
            and lines[curY][curX] == "."
        ):
            lines[curY][curX] = "#"
        newPos = newX, newY = curX + dX, curY + dY
        if newX in [-1, len(lines[0])] or newY in [-1, len(lines)]:
            continue
        if newPos not in mirs and lines[newY][newX] in ["|", "\\", "/", "-"]:
            mirs.add(newPos)
        if lines[newY][newX] == "|":
            if dX in [1, -1]:
                beams.append((newY, newX, 1, 0))
                beams.append((newY, newX, -1, 0))
                continue
        if lines[newY][newX] == "-":
            if dY in [1, -1]:
                beams.append((newY, newX, 0, 1))
                beams.append((newY, newX, 0, -1))
                continue
        elif lines[newY][newX] == "\\":
            if dX in [1, -1]:
                dY, dX = dX, 0
            else:
                dY, dX = 0, dY
        elif lines[newY][newX] == "/":
            if dX in [1, -1]:
                dY, dX = -1 * dX, 0
            else:
                dY, dX = 0, -1 * dY
        beams.append((newY, newX, dY, dX))
    return sum([sum([1 for i in j if i == "#"]) for j in lines]) + len(mirs)


def part1(filename):
    with open(filename,"r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]
    return getHashtags(lines, 0, -1, 0, 1)


def part2(filename):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    lines = [list(i) for i in lines]
    ans = 0
    for i in range(len(lines)):
        ans = max(
            ans,
            getHashtags(lines, i, -1, 0, 1),
            getHashtags(lines, i, len(lines[0]), 0, -1),
        )
    for j in range(len(lines[0])):
        ans = max(
            ans,
            getHashtags(lines, -1, j, 1, 0),
            getHashtags(lines, len(lines), j, -1, 0),
        )
    return ans


if __name__ == "__main__":
    import copy
    print(part1("Day 16/input.txt"))