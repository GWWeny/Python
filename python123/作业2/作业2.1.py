scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40,

          "Zhou Liu": 96,"Zhao Qi": 65, "Sun Ba": 90,

          "Zheng Jiu": 78, "Wu Shi": 99,"Dong Shiyi": 60}
highest_score=max(scores.values())
lowest_score=min(scores.values())
average_score=sum(scores.values())/len(scores)
top_student=[name for name,score in scores.items() if score==highest_score]
print(f"最高分是:{highest_score},最低分是{lowest_score},平均分是{average_score:.3f}")
print(f"最高分对应的学生是{'，'.join(top_student)}")
