from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time, os

# === Setup Driver ===
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=service, options=options)

# === Open Streamlit App ===
driver.get("http://localhost:8501")

# Wait until app is ready
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Climate Change Dashboard')]"))
)
print("✅ Page loaded successfully!")

# === Find the app's real tab buttons ===
time.sleep(3)
all_buttons = driver.find_elements(By.CSS_SELECTOR, "button[data-testid='stTab']")

print(f"🧭 Found {len(all_buttons)} real dashboard tabs.")

# === Screenshot folder ===
os.makedirs("screenshots", exist_ok=True)

# === Click each tab using JavaScript (bypass overlay) ===
for index, tab in enumerate(all_buttons, start=1):
    tab_name = tab.text.strip() or f"Tab_{index}"
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", tab)
        time.sleep(1)
        # Use JS click to avoid header interception
        driver.execute_script("arguments[0].click();", tab)
        print(f"✅ Clicked tab {index}: {tab_name}")
        time.sleep(2)
        screenshot_path = f"screenshots/tab_{index}_{tab_name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"📸 Screenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"⚠️ Could not click tab {index} ({tab_name}): {e}")

driver.quit()
print("🏁 UI Test Completed Successfully!")
