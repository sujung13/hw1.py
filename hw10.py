import os
import pickle

# 파일 경로 설정
score_file = 'score.bin'

def save_scores(scores):
    with open(score_file, 'wb') as f:
        pickle.dump(scores, f)

def load_scores():
    if os.path.exists(score_file):
        with open(score_file, 'rb') as f:
            scores = pickle.load(f)
        return scores
    return []

def main():
    scores = load_scores()

    if scores:
        print("[파일 읽기]")
    else:
        print("[점수 입력]")
        while True:
            try:
                score = int(input(f"# {len(scores) + 1}? "))
                if score < 0:
                    break
                scores.append(score)
            except ValueError:
                print("숫자를 입력해주세요.")

        save_scores(scores)

    if scores:
        print("[점수 출력]")
        print("개인점수:", ' '.join(map(str, scores)))
        print("평균:", sum(scores) / len(scores))
    else:
        print("저장된 점수가 없습니다.")

if __name__ == '__main__':
    main()
