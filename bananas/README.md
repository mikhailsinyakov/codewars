## Bananas

Given a string of letters `a`, `b`, `n` how many different ways can you make the word "<span style="color: yellow">banana</span>" by crossing out various letters and then reading left-to-right?

(Use `-` to indicate a crossed-out letter)

### Example
Input

    bbananana

Output

    b-anana--
    b-anan--a
    b-ana--na
    b-an--ana
    b-a--nana
    b---anana
    -banana--
    -banan--a
    -bana--na
    -ban--ana
    -ba--nana
    -b--anana

Notes:
- You must return all possible bananas, but the order does not matter
- The example output above is formatted for readability. Please refer to the example tests for expected format of your result.