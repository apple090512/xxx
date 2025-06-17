<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>요리 레시피 모음</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #fefefe;
      margin: 0;
      padding: 20px;
    }
    h1 {
      text-align: center;
      color: #444;
    }
    .category {
      margin-top: 40px;
      padding: 20px;
      border-radius: 10px;
      background-color: #f3f3f3;
    }
    .recipe {
      margin: 15px 0;
      padding: 15px;
      border-left: 5px solid #888;
      background-color: #fff;
      border-radius: 5px;
    }
    .recipe-title {
      font-size: 1.1em;
      font-weight: bold;
      margin-bottom: 5px;
    }
    .recipe-desc {
      font-size: 0.95em;
    }
  </style>
</head>
<body>

  <h1>🍽 요리 레시피 모음</h1>

  <div id="recipes-container"></div>

  <script>
    'use strict';

    const recipeData = {
      '서양 요리': [
        { title: '스파게티 볼로네제', desc: '다진 소고기와 토마토소스를 사용한 파스타입니다.' },
        { title: '치킨 알프레도', desc: '크림소스와 닭고기를 곁들인 부드러운 파스타 요리입니다.' },
        { title: '시저 샐러드', desc: '로메인과 파르메산 치즈, 크루통이 들어간 고전적인 샐러드.' },
        { title: '프렌치 어니언 수프', desc: '카라멜라이즈된 양파와 치즈를 얹은 따뜻한 수프입니다.' },
        { title: '비프 스테이크', desc: '굽기 정도를 선택해 조리하는 소고기 스테이크입니다.' }
      ],
      '한식 요리': [
        { title: '비빔밥', desc: '다양한 나물과 고기, 고추장을 비벼 먹는 한국 대표 음식.' },
        { title: '불고기', desc: '얇게 썬 쇠고기를 간장 양념에 재운 후 볶은 요리입니다.' },
        { title: '김치찌개', desc: '김치, 돼지고기, 두부 등을 넣고 끓인 찌개입니다.' },
        { title: '잡채', desc: '당면과 채소, 고기를 볶아 만든 잔칫날 인기 음식입니다.' },
        { title: '된장국', desc: '된장을 푼 국물에 두부, 미역 등을 넣은 전통 국요리.' }
      ]
    };

    const container = document.getElementById('recipes-container');

    for (const category in recipeData) {
      const section = document.createElement('div');
      section.className = 'category';

      const title = document.createElement('h2');
      title.textContent = category;
      section.appendChild(title);

      recipeData[category].forEach(recipe => {
        const recipeDiv = document.createElement('div');
        recipeDiv.className = 'recipe';

        recipeDiv.innerHTML = `
          <div class="recipe-title">${recipe.title}</div>
          <div class="recipe-desc">${recipe.desc}</div>
        `;

        section.appendChild(recipeDiv);
      });

      container.appendChild(section);
    }
  </script>

</body>
</html>
