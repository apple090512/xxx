<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>게임 공략 백과</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background-color: #f4f4f4;
    }
    h1, h2 {
      color: #333;
    }
    .genre {
      margin-bottom: 30px;
      background-color: #fff;
      padding: 15px;
      border-radius: 8px;
      box-shadow: 0 0 5px rgba(0,0,0,0.1);
    }
    .game {
      margin-left: 20px;
    }
  </style>
</head>
<body>

  <h1>🎮 게임 공략 백과</h1>
  <div id="game-guides"></div>

  <script>
    'use strict';

    // 게임 데이터 (분야별로 구성)
    const gameData = {
      'RPG': [
        {
          name: '엘든 링',
          guide: '보스전은 패턴 분석이 핵심이며, 회피 타이밍을 익히는 것이 중요합니다.'
        },
        {
          name: '파이널 판타지 7 리메이크',
          guide: 'ATB 게이지를 적극적으로 활용하고, 약점 속성에 맞는 마테리아를 세팅하세요.'
        }
      ],
      'FPS': [
        {
          name: '오버워치 2',
          guide: '팀 조합과 궁극기 운영이 중요합니다. 맵 지형을 활용하세요.'
        },
        {
          name: '콜 오브 듀티: 모던 워페어',
          guide: '소리 감지와 미니맵 활용을 통해 적 위치를 예측하세요.'
        }
      ],
      '액션': [
        {
          name: '세키로: 섀도우 다이 트와이스',
          guide: '패링(PARRY)이 전투의 핵심입니다. 타이밍 연습이 필요합니다.'
        }
      ]
    };

    const container = document.getElementById('game-guides');

    // 화면에 데이터 렌더링
    for (const genre in gameData) {
      const genreDiv = document.createElement('div');
      genreDiv.className = 'genre';

      const genreTitle = document.createElement('h2');
      genreTitle.textContent = genre;
      genreDiv.appendChild(genreTitle);

      gameData[genre].forEach(game => {
        const gameDiv = document.createElement('div');
        gameDiv.className = 'game';

        gameDiv.innerHTML = `<strong>${game.name}</strong>: ${game.guide}`;
        genreDiv.appendChild(gameDiv);
      });

      container.appendChild(genreDiv);
    }
  </script>
</body>
</html>
