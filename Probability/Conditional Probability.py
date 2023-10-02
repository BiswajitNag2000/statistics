box1_white_ball = 5
box1_black_ball = 7
box2_white_ball = 3
box2_black_ball = 12
coin_probability = 1 / 2
white_box2 = box2_white_ball / (box2_white_ball + box2_black_ball)
white_box1 = box1_white_ball / (box1_white_ball + box1_black_ball)
print(("box1 p(W|Tc) = ", round(white_box1, 2)),
      ("box2 p(W|T) = ", round(white_box2, 2)))
final_ans = (white_box2 * coin_probability) / (
  (white_box2 * coin_probability) + (white_box1 * coin_probability))
print(
  "bayes theorem formula P(T|W) = P(T ∩ W) P(W) = P(W|T)P(T) P(W|T)P(T) + P(W|Tc)P(Tc) = ",
  round(final_ans, 2)) 
print("probability that this ball was taken from box 2 is:",
      round(final_ans, 2))
