import json
from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel

app = FastAPI(docs_url="/api-docs")

class Prompt(BaseModel):
    prompt: str

@app.post("/interior/generate")
async def gen_image(body: str = Form(...), file: UploadFile = File(...)):
    
    prompt = Prompt(**json.loads(body))

    return [
  {
    "coordinate": [
      10,
      30
    ],
    "label": "소파",
    "image_url": "https://storage.googleapis.com/bbangggujipggu/detected_object/2024-07-28T19-45-33-540989bed",
    "items": [
      {
        "title": "에보니아 루비 2인 패브릭<b>소파</b>",
        "productUrl": "https://search.shopping.naver.com/catalog/8014189833",
        "price": "105600",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8014189/8014189833.20240503101626.jpg"
      },
      {
        "title": "에보니아 발리 1인용 <b>2인용</b> 쇼파의자 인조가죽 패브릭 미니 컴팩트 <b>소파</b>",
        "productUrl": "https://smartstore.naver.com/main/products/8835291397",
        "price": "57900",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8637979/86379791720.1.jpg"
      },
      {
        "title": "에보니아 뮤즈 2인 패브릭 <b>소파</b> 스툴포함",
        "productUrl": "https://search.shopping.naver.com/catalog/17309714958",
        "price": "136400",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_1730971/17309714958.20221018114919.jpg"
      },
      {
        "title": "동서가구 소프 바니 2인 아쿠아클린 <b>소파</b> DNA087",
        "productUrl": "https://search.shopping.naver.com/catalog/36139718621",
        "price": "197000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_3613971/36139718621.20221128094215.jpg"
      },
      {
        "title": "에보니아 라떼 2인 패브릭<b>소파</b>",
        "productUrl": "https://search.shopping.naver.com/catalog/8764943398",
        "price": "97870",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8764943/8764943398.20240503101453.jpg"
      },
      {
        "title": "보니애가구 조안 아쿠아텍스 2인 <b>소파</b>",
        "productUrl": "https://search.shopping.naver.com/catalog/24872433528",
        "price": "121000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_2487243/24872433528.20201117120512.jpg"
      },
      {
        "title": "라운드쇼파 조약돌 구름<b>소파</b> 수입 디자인쇼파 라운지 클라우드<b>소파</b>",
        "productUrl": "https://smartstore.naver.com/main/products/8142890346",
        "price": "665000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8568739/85687390669.1.jpg"
      },
      {
        "title": "퍼니코 하루 DIY 아쿠아텍스 2인 <b>소파</b>",
        "productUrl": "https://search.shopping.naver.com/catalog/41254288618",
        "price": "99000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_4125428/41254288618.20230718100335.jpg"
      },
      {
        "title": "보루네오 디에르 레이 아쿠아텍스 2인 <b>소파</b>",
        "productUrl": "https://search.shopping.naver.com/catalog/45941638619",
        "price": "209000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_4594163/45941638619.20240221143520.jpg"
      },
      {
        "title": "아이앤 블렌 아쿠아텍스 2인 <b>소파</b> 스툴포함 OB",
        "productUrl": "https://search.shopping.naver.com/catalog/45456187618",
        "price": "153600",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_4545618/45456187618.20240125153845.jpg"
      }
    ]
  },
  {
    "coordinate": [
      30,
      50
    ],
    "label": "침대",
    "image_url": "https://storage.googleapis.com/bbangggujipggu/detected_object/2024-07-28T19-45-35-265719couch",
    "items": [
      {
        "title": "슬립퍼 티라 <b>침대</b>프레임 슈퍼싱글 <b>퀸</b> 킹 라지킹 저상형 호텔 호텔형 <b>패브릭 침대</b>",
        "productUrl": "https://smartstore.naver.com/main/products/7761682726",
        "price": "387000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8530618/85306183048.4.jpg"
      },
      {
        "title": "퍼니코 빈 아쿠아텍스 <b>패브릭</b> 평상형 호텔 <b>침대</b> 프레임 슈퍼싱글 <b>퀸</b> 킹 라지킹 캘리포니아킹",
        "productUrl": "https://smartstore.naver.com/main/products/8536994771",
        "price": "249000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8608149/86081495094.7.jpg"
      },
      {
        "title": "데일리리빙 드레스덴 조야 <b>패브릭</b> 평상형 호텔식 <b>침대</b> 프레임 슈퍼싱글 <b>퀸</b> 킹 라지킹",
        "productUrl": "https://shopping.naver.com/outlink/itemdetail/9379107191",
        "price": "199000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8692360/86923607514.4.jpg"
      },
      {
        "title": "퍼니코 샤르망 앤틱 매립형 벨벳 <b>패브릭 침대</b> 슈퍼싱글 <b>퀸</b> 킹",
        "productUrl": "https://smartstore.naver.com/main/products/4596292335",
        "price": "259000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8214081/82140812552.7.jpg"
      },
      {
        "title": "웰퍼니쳐 위니 무선충전 LED 아쿠아텍스 <b>패브릭 침대</b> <b>퀸</b> Q",
        "productUrl": "https://smartstore.naver.com/main/products/9946201078",
        "price": "328000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8749070/87490703351.jpg"
      },
      {
        "title": "에덴느 호텔<b>침대</b>프레임 라지킹 이스턴킹 더블 <b>퀸</b> 트윈<b>베드</b> 신혼부부",
        "productUrl": "https://smartstore.naver.com/main/products/6742357888",
        "price": "489000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8428685/84286858210.4.jpg"
      },
      {
        "title": "커브 <b>패브릭 침대</b>프레임 슈퍼싱글 <b>퀸</b> 킹 라지킹 Q SS K LK",
        "productUrl": "https://smartstore.naver.com/main/products/9199845183",
        "price": "886000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8674434/86744345506.jpg"
      },
      {
        "title": "평상형 <b>침대</b>프레임 파운데이션 슈퍼싱글 <b>퀸</b> 킹 라지킹 저상형 무헤드 <b>침대</b> 깔판",
        "productUrl": "https://smartstore.naver.com/main/products/5048517273",
        "price": "262000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8259303/82593038357.11.jpg"
      },
      {
        "title": "밀레 호텔<b>침대</b> 프레임 <b>패브릭</b> 호텔식 라지킹 <b>퀸</b> 킹 트윈<b>침대</b> 평상형 led",
        "productUrl": "https://smartstore.naver.com/main/products/10353988847",
        "price": "589000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8789849/87898493320.1.jpg"
      },
      {
        "title": "퍼니코 다나 모던 매립형 벨벳 <b>패브릭 침대</b> 프레임 슈퍼싱글/<b>퀸</b>",
        "productUrl": "https://smartstore.naver.com/main/products/5974927747",
        "price": "219000",
        "imageUrl": "https://shopping-phinf.pstatic.net/main_8351942/83519427235.6.jpg"
      }
    ]
  }
]