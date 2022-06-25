def run():
    import streamlit as st
    from PIL import Image


    with open("style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.title("😁 Teeth checking tool")
    st.subheader("Искусственный интеллект для анализа состояния зубов по фотографии")
    uploaded_files = st.file_uploader(
        "Выберите изображение...",
        accept_multiple_files=True,
        type=["jpg", "png", "jpeg"],
    )

    def to_black_and_white(img):
        with st.spinner("Обработка..."):
            img_grey = img.convert("L")
            st.success("Готово!")
        return img_grey

    with st.empty():
        if st.button("Проверить!"):
            if not uploaded_files:
                st.warning("Пожалуйста, выберите файлы для обработки")
            else:
                for uploaded_file in uploaded_files:
                    image = Image.open(uploaded_file)
                    bw_img = to_black_and_white(image)
                    st.image(bw_img, caption=uploaded_file.name)


if __name__ == "__main__":
    run()
