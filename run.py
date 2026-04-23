import run

if __name__ == "__main__":
    try:
        run.main()
    except AttributeError:
        # တကယ်လို့ main() function ကို တိုက်ရိုက်ခေါ်မရရင် 
        # ဒါက script ထဲမှာတင် logic တွေ run ဖို့ လုပ်ထားတာဖြစ်ပါလိမ့်မယ်
        pass
    except KeyboardInterrupt:
        exit()
      
