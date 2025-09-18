import { main } from './index'

const test_cases: { input: number[]; want: number }[] = [
  { input: [1, 2, 3], want: 6 },
  { input: [0, 0, 0], want: 0 },
  { input: [-1, -2, -3], want: -6 },
  { input: [10, 20, 30], want: 60 },
  { input: [], want: 0 },
]

describe('sumArray', () => {
  test.each(test_cases)('return $want when input is $input', ({ input, want }) => {
    expect(main(input)).toBe(want)
  })
})
