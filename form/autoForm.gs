function createEventForm() {
  const form = FormApp.create("ユーザーアンケート");
  const id = PropertiesService.getScriptProperties().getProperty("FOLDER_ID");
  const formFile = DriveApp.getFileById(form.getId());

  var spreadsheetId = "1n-2TK0VExxgwrGim8K30vm587fOA7AhHFiD_iMqdFAA";
  var sheetName = "フォームの回答 1";

  var spreadsheet = SpreadsheetApp.openById(spreadsheetId);
  var sheet = spreadsheet.getSheetByName(sheetName);
  var allData = sheet.getDataRange().getValues();

  // 固定設問
  //form.addMultipleChoiceItem()
  //  .setTitle('行きたいですか？')
  //  .setChoiceValues(['行きたい', '行きたくない'])
  //  .setRequired(true);

  form
    .addMultipleChoiceItem()
    .setTitle("年代")
    .setChoiceValues(["10代", "20代", "30代", "40代", "50代", "60代", "70代"])
    .setRequired(true);

  form
    .addMultipleChoiceItem()
    .setTitle("性別")
    .setChoiceValues(["男性", "女性", "それ以外", "未回答"])
    .setRequired(true);

  form
    .addMultipleChoiceItem()
    .setTitle("希望するサイズ")
    .setChoiceValues([
      "男性S",
      "男性M",
      "男性L",
      "男性Sより小さい",
      "男性Lより大きい",
      "女性S",
      "女性M",
      "女性L",
      "女性Sより小さい",
      "女性Lより大きい",
    ])
    .setRequired(true);

  // 月のリストを取得（D列のデータ）
  var months = allData
    .map(function (row) {
      return row[3]; // D列のインデックスは0から数えて3
    })
    .slice(1); // 1行目はヘッダなので除外

  var shops = allData
    .map(function (row) {
      return row[1]; // B列のインデックスは1
    })
    .slice(1); // 1行目はヘッダなので除外

  // 4月に出店可能な店が存在する場合に質問項目を追加
  var aprilShops = [];
  for (var i = 0; i < shops.length; i++) {
    if (months[i].includes("4月")) {
      aprilShops.push(shops[i]);
    }
  }

  if (aprilShops.length > 0) {
    var item_April = form
      .addCheckboxItem()
      .setTitle("4月に出店可能な店です。2つ選択してください。")
      .setChoiceValues(aprilShops)
      .setRequired(true);
  }

  // 5月に出店可能な店が存在する場合に質問項目を追加
  var mayShops = [];
  for (var i = 0; i < shops.length; i++) {
    if (months[i].includes("5月")) {
      mayShops.push(shops[i]);
    }
  }

  if (mayShops.length > 0) {
    var item_May = form
      .addCheckboxItem()
      .setTitle("5月に出店可能な店です。2つ選択してください。")
      .setChoiceValues(mayShops)
      .setRequired(true);
  }

  // 6月に出店可能な店が存在する場合に質問項目を追加
  var juneShops = [];
  for (var i = 0; i < shops.length; i++) {
    if (months[i].includes("6月")) {
      juneShops.push(shops[i]);
    }
  }

  if (juneShops.length > 0) {
    var item_June = form
      .addCheckboxItem()
      .setTitle("6月に出店可能な店です。2つ選択してください。")
      .setChoiceValues(juneShops)
      .setRequired(true);
  }

  // 以下同様に他の月に関する処理を追加していくことができます

  // フォームの回答を受けるためのスプレッドシートを作成
  var outspreadsheet = SpreadsheetApp.create("フォーム回答データ");

  // フォームとスプレッドシートを関連付ける
  form.setDestination(
    FormApp.DestinationType.SPREADSHEET,
    outspreadsheet.getId()
  );

  // フォームを公開
  var formUrl = form.getPublishedUrl();
  Logger.log("フォームが作成されました。公開URL: " + formUrl);

  // スプレッドシートのURLをログに表示
  var sheetUrl = outspreadsheet.getUrl();
  Logger.log("フォームの回答データが保存されるスプレッドシート: " + sheetUrl);
}
