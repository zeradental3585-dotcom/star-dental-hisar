/**
 * Star Dental Clinic (Hisar) — website lead logger
 *
 * Bound to the "Star Dental Hisar — Leads" Google Sheet. Receives POSTs
 * from the site's assets/js/main.js and appends one row per lead event
 * to a "Leads" tab (created automatically the first time this runs).
 *
 * Deploy: Extensions > Apps Script > paste this in as Code.gs > Deploy >
 * New deployment > type "Web app" > Execute as "Me" > Who has access
 * "Anyone" > Deploy. Copy the resulting /exec URL into
 * assets/js/main.js's LEAD_WEBHOOK_URL constant.
 */

var SHEET_NAME = "Leads";
var HEADERS = [
  "Timestamp",
  "Type",
  "Page",
  "Name",
  "Phone",
  "Interest",
  "Message",
  "CTA",
  "Referrer",
];

function getLeadsSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold");
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function doPost(e) {
  try {
    var raw = (e && e.postData && e.postData.contents) || "{}";
    var data = JSON.parse(raw);
    var sheet = getLeadsSheet_();
    sheet.appendRow([
      new Date(),
      data.type || "",
      data.page || "",
      data.name || "",
      data.phone || "",
      data.interest || "",
      data.message || "",
      data.cta || "",
      data.referrer || "",
    ]);
    return ContentService
      .createTextOutput(JSON.stringify({ result: "success" }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: "error", error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Lets you sanity-check the deployment by opening the /exec URL directly
// in a browser — should show a small JSON status message.
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: "Star Dental Hisar lead logger is live" }))
    .setMimeType(ContentService.MimeType.JSON);
}
